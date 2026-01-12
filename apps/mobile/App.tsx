import { useEffect, useState, useCallback } from 'react'
import { StatusBar } from 'expo-status-bar'
import { StyleSheet, Text, View, TouchableOpacity, FlatList, RefreshControl } from 'react-native'
import * as Linking from 'expo-linking'
import { APP_NAME, APP_VERSION, MOOD_COLORS, type CaptureMetadata } from '@moments/shared'
import { CaptureToast } from './src/components/CaptureToast'
import { createCapture, getCaptures } from './src/lib/capture'
import { syncPendingCaptures, getPendingCount } from './src/lib/offlineQueue'

type ToastStatus = 'saving' | 'saved' | 'archived' | 'error'

export default function App() {
  const [captures, setCaptures] = useState<CaptureMetadata[]>([])
  const [refreshing, setRefreshing] = useState(false)
  const [pendingCount, setPendingCount] = useState(0)
  const [toast, setToast] = useState<{ visible: boolean; status: ToastStatus; message?: string }>({
    visible: false,
    status: 'saved',
  })

  const loadCaptures = useCallback(async () => {
    const data = await getCaptures()
    setCaptures(data)
    const pending = await getPendingCount()
    setPendingCount(pending)
  }, [])

  const handleRefresh = useCallback(async () => {
    setRefreshing(true)
    await syncPendingCaptures()
    await loadCaptures()
    setRefreshing(false)
  }, [loadCaptures])

  const handleDeepLink = useCallback(
    async (url: string) => {
      const parsed = Linking.parse(url)
      if (parsed.path === 'capture' && parsed.queryParams?.url) {
        const targetUrl = parsed.queryParams.url as string
        setToast({ visible: true, status: 'saving' })

        const result = await createCapture({
          url: targetUrl,
          title: (parsed.queryParams.title as string) || undefined,
        })

        if (result.success) {
          setToast({ visible: true, status: 'saved' })
          await loadCaptures()
        } else {
          setToast({ visible: true, status: 'error', message: result.error })
        }

        setTimeout(() => setToast((prev) => ({ ...prev, visible: false })), 2000)
      }
    },
    [loadCaptures]
  )

  useEffect(() => {
    loadCaptures()

    const subscription = Linking.addEventListener('url', (event) => {
      handleDeepLink(event.url)
    })

    Linking.getInitialURL().then((url) => {
      if (url) handleDeepLink(url)
    })

    return () => subscription.remove()
  }, [handleDeepLink, loadCaptures])

  const renderCapture = ({ item }: { item: CaptureMetadata }) => (
    <View style={[styles.captureCard, { borderLeftColor: MOOD_COLORS[item.moodColor || 'curiosity'] }]}>
      <Text style={styles.captureTitle} numberOfLines={1}>
        {item.title}
      </Text>
      <Text style={styles.captureUrl} numberOfLines={1}>
        {item.url}
      </Text>
      <View style={styles.captureFooter}>
        <Text style={styles.captureDate}>
          {item.capturedAt.toLocaleDateString()}
        </Text>
        <Text style={styles.captureStatus}>
          {item.status === 'saved' ? '✓' : item.status === 'archived' ? '✓✓' : '⏳'}
        </Text>
      </View>
    </View>
  )

  return (
    <View style={styles.container}>
      <CaptureToast {...toast} />

      <View style={styles.header}>
        <Text style={styles.title}>{APP_NAME}</Text>
        <Text style={styles.version}>v{APP_VERSION}</Text>
        {pendingCount > 0 && (
          <Text style={styles.pendingBadge}>{pendingCount} pending</Text>
        )}
      </View>

      <View style={styles.moodContainer}>
        {Object.entries(MOOD_COLORS).map(([name, color]) => (
          <View key={name} style={[styles.moodDot, { backgroundColor: color }]} />
        ))}
      </View>

      {captures.length === 0 ? (
        <View style={styles.emptyState}>
          <Text style={styles.emptyIcon}>🌟</Text>
          <Text style={styles.emptyTitle}>Your Digital Darkroom</Text>
          <Text style={styles.emptyText}>
            Share any URL to Moments to start{'\n'}capturing your knowledge journey
          </Text>
        </View>
      ) : (
        <FlatList
          data={captures}
          renderItem={renderCapture}
          keyExtractor={(item) => item.id}
          style={styles.list}
          contentContainerStyle={styles.listContent}
          refreshControl={
            <RefreshControl
              refreshing={refreshing}
              onRefresh={handleRefresh}
              tintColor="#6b7280"
            />
          }
        />
      )}

      <StatusBar style="light" />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0a0a0f',
  },
  header: {
    paddingTop: 60,
    paddingHorizontal: 24,
    paddingBottom: 16,
    alignItems: 'center',
  },
  title: {
    fontSize: 28,
    fontWeight: '700',
    color: '#ffffff',
    marginBottom: 4,
  },
  version: {
    fontSize: 14,
    color: '#6b7280',
  },
  pendingBadge: {
    marginTop: 8,
    fontSize: 12,
    color: '#eab308',
    backgroundColor: 'rgba(234, 179, 8, 0.1)',
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
  },
  moodContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 12,
    marginVertical: 16,
  },
  moodDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
  },
  emptyState: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 40,
  },
  emptyIcon: {
    fontSize: 48,
    marginBottom: 16,
  },
  emptyTitle: {
    fontSize: 20,
    fontWeight: '600',
    color: '#ffffff',
    marginBottom: 8,
  },
  emptyText: {
    fontSize: 16,
    color: '#6b7280',
    textAlign: 'center',
    lineHeight: 24,
  },
  list: {
    flex: 1,
  },
  listContent: {
    padding: 16,
    gap: 12,
  },
  captureCard: {
    backgroundColor: '#1a1a24',
    borderRadius: 12,
    padding: 16,
    borderLeftWidth: 4,
  },
  captureTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#ffffff',
    marginBottom: 4,
  },
  captureUrl: {
    fontSize: 13,
    color: '#6b7280',
    marginBottom: 12,
  },
  captureFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  captureDate: {
    fontSize: 12,
    color: '#4b5563',
  },
  captureStatus: {
    fontSize: 14,
    color: '#22c55e',
  },
})
