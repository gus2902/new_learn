import AsyncStorage from '@react-native-async-storage/async-storage'
import type { MoodColor } from '@moments/shared'
import { createCapture } from './capture'

interface PendingCapture {
  id: string
  url: string
  title?: string
  moodColor?: MoodColor
  capturedAt: string
  retryCount: number
}

const PENDING_KEY = 'moments:pending_captures'
const MAX_RETRIES = 3

export async function queueCapture(capture: Omit<PendingCapture, 'id' | 'retryCount'>): Promise<string> {
  const id = `capture_${Date.now()}_${Math.random().toString(36).slice(2, 9)}`
  
  const pending: PendingCapture = {
    ...capture,
    id,
    retryCount: 0,
  }

  const existing = await getPendingCaptures()
  await AsyncStorage.setItem(PENDING_KEY, JSON.stringify([...existing, pending]))

  return id
}

export async function getPendingCaptures(): Promise<PendingCapture[]> {
  const data = await AsyncStorage.getItem(PENDING_KEY)
  return data ? JSON.parse(data) : []
}

export async function removePendingCapture(id: string): Promise<void> {
  const existing = await getPendingCaptures()
  const filtered = existing.filter((c) => c.id !== id)
  await AsyncStorage.setItem(PENDING_KEY, JSON.stringify(filtered))
}

export async function syncPendingCaptures(): Promise<{ synced: number; failed: number }> {
  const pending = await getPendingCaptures()
  let synced = 0
  let failed = 0

  for (const capture of pending) {
    const result = await createCapture({
      url: capture.url,
      title: capture.title,
      moodColor: capture.moodColor,
    })

    if (result.success) {
      await removePendingCapture(capture.id)
      synced++
    } else {
      if (capture.retryCount >= MAX_RETRIES) {
        await removePendingCapture(capture.id)
        failed++
      } else {
        await updateRetryCount(capture.id, capture.retryCount + 1)
      }
    }
  }

  return { synced, failed }
}

async function updateRetryCount(id: string, retryCount: number): Promise<void> {
  const existing = await getPendingCaptures()
  const updated = existing.map((c) => (c.id === id ? { ...c, retryCount } : c))
  await AsyncStorage.setItem(PENDING_KEY, JSON.stringify(updated))
}

export async function getPendingCount(): Promise<number> {
  const pending = await getPendingCaptures()
  return pending.length
}
