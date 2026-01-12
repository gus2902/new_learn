import React from 'react'
import { View, Text, StyleSheet, Animated } from 'react-native'
import { MOOD_COLORS } from '@moments/shared'

interface CaptureToastProps {
  visible: boolean
  status: 'saving' | 'saved' | 'archived' | 'error'
  message?: string
}

export function CaptureToast({ visible, status, message }: CaptureToastProps) {
  const opacity = React.useRef(new Animated.Value(0)).current

  React.useEffect(() => {
    Animated.timing(opacity, {
      toValue: visible ? 1 : 0,
      duration: 200,
      useNativeDriver: true,
    }).start()
  }, [visible, opacity])

  const getStatusIcon = () => {
    switch (status) {
      case 'saving':
        return '⏳'
      case 'saved':
        return '✓'
      case 'archived':
        return '✓✓'
      case 'error':
        return '✗'
    }
  }

  const getStatusText = () => {
    switch (status) {
      case 'saving':
        return 'Saving...'
      case 'saved':
        return 'Saved'
      case 'archived':
        return 'Permanently Archived'
      case 'error':
        return message || 'Failed to save'
    }
  }

  const getStatusColor = () => {
    switch (status) {
      case 'saving':
        return MOOD_COLORS.curiosity
      case 'saved':
        return MOOD_COLORS.peace
      case 'archived':
        return MOOD_COLORS.inspiration
      case 'error':
        return MOOD_COLORS.passion
    }
  }

  if (!visible) return null

  return (
    <Animated.View style={[styles.container, { opacity }]}>
      <View style={[styles.toast, { borderLeftColor: getStatusColor() }]}>
        <Text style={styles.icon}>{getStatusIcon()}</Text>
        <Text style={styles.text}>{getStatusText()}</Text>
      </View>
    </Animated.View>
  )
}

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    top: 60,
    left: 20,
    right: 20,
    alignItems: 'center',
    zIndex: 1000,
  },
  toast: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1a1a24',
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 12,
    borderLeftWidth: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
  },
  icon: {
    fontSize: 18,
    marginRight: 10,
  },
  text: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: '500',
  },
})
