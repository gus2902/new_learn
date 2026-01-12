export const APP_NAME = 'Moments: Mind Studio'
export const APP_VERSION = '0.0.1'

export interface CaptureMetadata {
  id: string
  url: string
  title: string
  description?: string
  capturedAt: Date
  moodColor?: MoodColor
  status: CaptureStatus
}

export type MoodColor = 'curiosity' | 'inspiration' | 'peace' | 'passion' | 'reflection'

export type CaptureStatus = 'pending' | 'saved' | 'archived' | 'failed'

export const MOOD_COLORS: Record<MoodColor, string> = {
  curiosity: '#3B82F6',
  inspiration: '#EAB308',
  peace: '#22C55E',
  passion: '#EF4444',
  reflection: '#A855F7',
}

export const CAPTURE_TIMEOUT_MS = 2000
export const ARCHIVE_TIMEOUT_MS = 30000
