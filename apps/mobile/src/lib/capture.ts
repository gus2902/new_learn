import { supabase } from './supabase'
import type { CaptureMetadata, MoodColor, CaptureStatus } from '@moments/shared'

interface CaptureInput {
  url: string
  title?: string
  description?: string
  moodColor?: MoodColor
}

interface CaptureResult {
  success: boolean
  id?: string
  error?: string
}

export async function createCapture(input: CaptureInput): Promise<CaptureResult> {
  const startTime = Date.now()

  try {
    const {
      data: { user },
    } = await supabase.auth.getUser()

    if (!user) {
      return { success: false, error: 'Not authenticated' }
    }

    const { data, error } = await supabase
      .from('captures')
      .insert({
        user_id: user.id,
        url: input.url,
        title: input.title || 'Untitled',
        description: input.description,
        mood_color: input.moodColor || 'curiosity',
        status: 'saved' as CaptureStatus,
        captured_at: new Date().toISOString(),
      })
      .select('id')
      .single()

    const elapsed = Date.now() - startTime
    console.log(`[Capture] Completed in ${elapsed}ms`)

    if (error) {
      return { success: false, error: error.message }
    }

    return { success: true, id: data.id }
  } catch (err) {
    return { success: false, error: String(err) }
  }
}

export async function getCaptures(limit = 20): Promise<CaptureMetadata[]> {
  const { data, error } = await supabase
    .from('captures')
    .select('*')
    .order('captured_at', { ascending: false })
    .limit(limit)

  if (error) {
    console.error('[Capture] Failed to fetch:', error)
    return []
  }

  return data.map((row) => ({
    id: row.id,
    url: row.url,
    title: row.title,
    description: row.description,
    capturedAt: new Date(row.captured_at),
    moodColor: row.mood_color,
    status: row.status,
  }))
}

export async function syncPendingCaptures(): Promise<number> {
  return 0
}
