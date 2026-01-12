import { StatusBar } from 'expo-status-bar'
import { StyleSheet, Text, View } from 'react-native'
import { APP_NAME, APP_VERSION, MOOD_COLORS } from '@moments/shared'

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{APP_NAME}</Text>
      <Text style={styles.version}>v{APP_VERSION}</Text>
      <View style={styles.moodContainer}>
        {Object.entries(MOOD_COLORS).map(([name, color]) => (
          <View key={name} style={[styles.moodDot, { backgroundColor: color }]} />
        ))}
      </View>
      <Text style={styles.status}>Phase 0: PoC Ready</Text>
      <StatusBar style="light" />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0a0a0f',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 28,
    fontWeight: '700',
    color: '#ffffff',
    marginBottom: 8,
  },
  version: {
    fontSize: 14,
    color: '#6b7280',
    marginBottom: 24,
  },
  moodContainer: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 32,
  },
  moodDot: {
    width: 16,
    height: 16,
    borderRadius: 8,
  },
  status: {
    fontSize: 16,
    color: '#22c55e',
    fontWeight: '500',
  },
})
