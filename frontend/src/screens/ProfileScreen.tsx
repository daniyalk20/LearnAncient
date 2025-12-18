import React, { useEffect, useState } from "react";
import { AuthTokens, login } from "../api";

const STORAGE_KEY = "learnancient-auth";

export const ProfileScreen: React.FC = () => {
  const [tokens, setTokens] = useState<AuthTokens | null>(null);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [status, setStatus] = useState<string | null>(null);

  useEffect(() => {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      try {
        setTokens(JSON.parse(raw));
      } catch {
        // ignore
      }
    }
  }, []);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus(null);
    try {
      const t = await login(username, password);
      setTokens(t);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(t));
      setStatus("Signed in successfully.");
    } catch (err) {
      console.error(err);
      setStatus("Login failed. Check your credentials.");
    }
  };

  const handleLogout = () => {
    setTokens(null);
    localStorage.removeItem(STORAGE_KEY);
  };

  return (
    <div className="card">
      <div className="card-header">
        <div>
          <div className="card-title">Profile & Preferences</div>
          <div className="card-subtitle">Authentication and display options</div>
        </div>
        <span className="badge">{tokens ? "Signed in" : "Guest"}</span>
      </div>

      {!tokens ? (
        <form onSubmit={handleLogin} aria-label="Sign in form">
          <div className="form-row">
            <label className="field-label" htmlFor="username">
              Username
            </label>
            <input
              id="username"
              className="input"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              autoComplete="username"
              required
            />
          </div>
          <div className="form-row">
            <label className="field-label" htmlFor="password">
              Password
            </label>
            <input
              id="password"
              type="password"
              className="input"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              autoComplete="current-password"
              required
            />
          </div>
          <button type="submit" className="primary-btn">
            Sign in
          </button>
          {status && <p className="text-muted" style={{ marginTop: 8 }}>{status}</p>}
        </form>
      ) : (
        <>
          <p className="text-muted" style={{ marginBottom: 12 }}>
            You are signed in. Review progress and SRS are now available.
          </p>
          <button type="button" className="primary-btn" onClick={handleLogout}>
            Sign out
          </button>
        </>
      )}
    </div>
  );
};
