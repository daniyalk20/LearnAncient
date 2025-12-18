import React, { useEffect, useState } from "react";
import { fetchReviewDue, ReviewItemDto, sendReviewAnswer } from "../api";

const STORAGE_KEY = "learnancient-auth";

export const ReviewScreen: React.FC = () => {
  const [items, setItems] = useState<ReviewItemDto[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [accessToken, setAccessToken] = useState<string | null>(null);

  useEffect(() => {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      try {
        const parsed = JSON.parse(raw) as { access: string };
        setAccessToken(parsed.access);
      } catch {
        // ignore
      }
    }
  }, []);

  useEffect(() => {
    if (!accessToken) return;
    setLoading(true);
    setError(null);
    fetchReviewDue(accessToken)
      .then((res) => setItems(res.items))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [accessToken]);

  const handleAnswer = async (quality: number) => {
    if (!accessToken || !items.length) return;
    const current = items[0];
    try {
      await sendReviewAnswer(accessToken, current.id, quality);
      setItems((prev) => prev.slice(1));
    } catch (err) {
      console.error(err);
      setError("Failed to submit answer");
    }
  };

  const current = items[0] ?? null;

  return (
    <div className="card">
      <div className="card-header">
        <div>
          <div className="card-title">Review: Spaced Repetition</div>
          <div className="card-subtitle">Vocabulary & forms</div>
        </div>
        <span className="badge">SRS</span>
      </div>

      {!accessToken && (
        <p className="text-muted">
          Sign in on the Profile tab to start reviewing due items.
        </p>
      )}

      {accessToken && loading && <p className="text-muted">Loading due items...</p>}
      {accessToken && error && <p className="text-muted">Error: {error}</p>}

      {accessToken && !loading && !error && !current && (
        <p className="text-muted">No items due right now. Great job!</p>
      )}

      {accessToken && current && (
        <>
          <p className="text-muted">
            Due items: {items.length} &middot; Passage: {current.passage_reference}
          </p>
          <div className="token-chip token-chip-selected" style={{ marginTop: 8 }}>
            {current.text}
          </div>
          <p className="text-muted" style={{ marginTop: 12 }}>
            How well did you recall this item?
          </p>
          <div style={{ display: "flex", gap: 8, marginTop: 6 }}>
            <button
              type="button"
              className="primary-btn"
              onClick={() => handleAnswer(1)}
            >
              Again
            </button>
            <button
              type="button"
              className="primary-btn"
              onClick={() => handleAnswer(3)}
            >
              Hard
            </button>
            <button
              type="button"
              className="primary-btn"
              onClick={() => handleAnswer(5)}
            >
              Easy
            </button>
          </div>
        </>
      )}
    </div>
  );
};
