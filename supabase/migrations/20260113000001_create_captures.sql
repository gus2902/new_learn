-- Captures table for storing URL captures
create table if not exists public.captures (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references auth.users(id) on delete cascade,
    url text not null,
    title text,
    description text,
    mood_color text default 'curiosity' check (mood_color in ('curiosity', 'inspiration', 'peace', 'passion', 'reflection')),
    status text default 'pending' check (status in ('pending', 'saved', 'archived', 'failed')),
    metadata jsonb default '{}',
    archive_path text,
    captured_at timestamptz default now(),
    archived_at timestamptz,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

-- Enable RLS
alter table public.captures enable row level security;

-- RLS Policies
create policy "Users can view own captures"
    on public.captures for select
    using (auth.uid() = user_id);

create policy "Users can insert own captures"
    on public.captures for insert
    with check (auth.uid() = user_id);

create policy "Users can update own captures"
    on public.captures for update
    using (auth.uid() = user_id);

create policy "Users can delete own captures"
    on public.captures for delete
    using (auth.uid() = user_id);

-- Indexes
create index if not exists captures_user_id_idx on public.captures(user_id);
create index if not exists captures_status_idx on public.captures(status);
create index if not exists captures_captured_at_idx on public.captures(captured_at desc);
create index if not exists captures_mood_color_idx on public.captures(mood_color);

-- Updated at trigger
create or replace function public.handle_updated_at()
returns trigger as $$
begin
    new.updated_at = now();
    return new;
end;
$$ language plpgsql;

create trigger captures_updated_at
    before update on public.captures
    for each row
    execute function public.handle_updated_at();
