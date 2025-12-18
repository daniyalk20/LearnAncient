import React, { useEffect, useState } from "react";
import { fetchLanguages, fetchPassage, Language, Passage, Token } from "../api";

export const ReadScreen: React.FC = () => {
  const [languages, setLanguages] = useState<Language[]>([]);
  const [passage, setPassage] = useState<Passage | null>(null);
  const [selectedToken, setSelectedToken] = useState<Token | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchLanguages()
      .then(setLanguages)
      .catch((err) => setError(err.message));

    fetchPassage(1)
      .then((p) => {
        setPassage(p);
        setSelectedToken(p.tokens[0] ?? null);
      })
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div className="card" aria-label="Reader module">
      <div className="card-header">
        <div>
          <div className="card-title">Read: Sample Manuscript</div>
          <div className="card-subtitle">
            {passage ? passage.reference : "Loading passage..."}
          </div>
        </div>
        <span className="badge">
          {languages.length ? languages[0].name : "Loading language..."}
        </span>
      </div>

      {error && <p className="text-muted">Error: {error}</p>}

      <div className="token-grid" aria-label="Token list">
        {passage?.tokens.map((t) => (
          <button
            key={t.id}
            type="button"
            className={
              "token-chip" + (selectedToken?.id === t.id ? " token-chip-selected" : "")
            }
            onClick={() => setSelectedToken(t)}
          >
            {t.text}
          </button>
        ))}
      </div>

      {selectedToken && (
        <div className="token-details" aria-live="polite">
          <div className="field-label">Surface</div>
          <div className="field-value">{selectedToken.text}</div>

          {selectedToken.lemma && (
            <>
              <div className="field-label" style={{ marginTop: 6 }}>
                Lemma
              </div>
              <div className="field-value">
                {selectedToken.lemma.lemma}
                {selectedToken.lemma.gloss && ` – ${selectedToken.lemma.gloss}`}
              </div>
            </>
          )}

          {selectedToken.morphology && (
            <>
              <div className="field-label" style={{ marginTop: 6 }}>
                Morphology
              </div>
              <div className="field-value">
                {selectedToken.morphology.tag} – {selectedToken.morphology.description}
              </div>
            </>
          )}

          {selectedToken.gloss && (
            <>
              <div className="field-label" style={{ marginTop: 6 }}>
                Gloss
              </div>
              <div className="field-value">{selectedToken.gloss}</div>
            </>
          )}
        </div>
      )}
    </div>
  );
};
