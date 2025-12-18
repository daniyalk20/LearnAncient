export const API_BASE = "/api/v1";

export interface Language {
  id: number;
  code: string;
  name: string;
}

export interface Token {
  id: number;
  index: number;
  text: string;
  gloss?: string;
  lemma?: { lemma: string; gloss?: string };
  morphology?: { tag: string; description: string };
}

export interface Passage {
  id: number;
  reference: string;
  content: string;
  tokens: Token[];
}

export interface AuthTokens {
  access: string;
  refresh: string;
}

export interface ReviewItemDto {
  id: number;
  token_id: number;
  text: string;
  passage_reference: string;
  due: string;
}

export interface ReviewDueResponse {
  items: ReviewItemDto[];
}

export async function fetchLanguages(): Promise<Language[]> {
  const res = await fetch(`${API_BASE}/languages`);
  if (!res.ok) throw new Error("Failed to load languages");
  return res.json();
}

export async function fetchPassage(id: number): Promise<Passage> {
  const res = await fetch(`${API_BASE}/reader/passage/${id}`);
  if (!res.ok) throw new Error("Failed to load passage");
  return res.json();
}

export async function login(username: string, password: string): Promise<AuthTokens> {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  if (!res.ok) throw new Error("Login failed");
  return res.json();
}

export async function fetchReviewDue(accessToken: string): Promise<ReviewDueResponse> {
  const res = await fetch(`${API_BASE}/review/due`, {
    headers: { Authorization: `Bearer ${accessToken}` }
  });
  if (!res.ok) throw new Error("Failed to load review queue");
  return res.json();
}

export async function sendReviewAnswer(
  accessToken: string,
  itemId: number,
  quality: number
): Promise<{ next_due: string }> {
  const res = await fetch(`${API_BASE}/review/answer`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`
    },
    body: JSON.stringify({ item_id: itemId, quality })
  });
  if (!res.ok) throw new Error("Failed to submit answer");
  return res.json();
}
