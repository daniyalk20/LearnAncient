import React from "react";

export const LearnScreen: React.FC = () => {
  return (
    <div className="card">
      <div className="card-header">
        <div>
          <div className="card-title">Learn: Foundations</div>
          <div className="card-subtitle">Alphabet → grammar → syntax</div>
        </div>
        <span className="badge">Guided Path</span>
      </div>
      <p className="text-muted">
        Structured lessons coming soon. For now, start by reading the
        sample passage in the Read tab and exploring each token.
      </p>
    </div>
  );
};
