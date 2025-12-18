import React from "react";

export const LibraryScreen: React.FC = () => {
  return (
    <div className="card">
      <div className="card-header">
        <div>
          <div className="card-title">Library & Reference</div>
          <div className="card-subtitle">Lexicon, morphology charts, grammar</div>
        </div>
        <span className="badge">Reference</span>
      </div>
      <p className="text-muted">
        In later phases, this space will hold lexicon lookups and cross-
        linked grammar references from the reader.
      </p>
    </div>
  );
};
