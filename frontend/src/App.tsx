import React, { useEffect, useState } from "react";
import { LearnScreen } from "./screens/LearnScreen";
import { ReadScreen } from "./screens/ReadScreen";
import { ReviewScreen } from "./screens/ReviewScreen";
import { LibraryScreen } from "./screens/LibraryScreen";
import { ProfileScreen } from "./screens/ProfileScreen";

export type TabKey = "learn" | "read" | "review" | "library" | "profile";

const NEXT_STEP_LABEL: Record<TabKey, string> = {
    learn: "Continue lesson",
    read: "Open current passage",
    review: "Review due cards",
    library: "Browse reference",
    profile: "Adjust preferences"
};

const TAB_META: Record<
    TabKey,
    {
        label: string;
        description: string;
    }
> = {
    learn: {
        label: "Learn",
        description: "Step–by–step lessons to build reading fluency."
    },
    read: {
        label: "Read",
        description: "Move through authentic texts with inline helps."
    },
    review: {
        label: "Review",
        description: "Spaced‑repetition cards to keep forms sticky."
    },
    library: {
        label: "Library",
        description: "Browse reference grammars, vocab, and resources."
    },
    profile: {
        label: "Profile",
        description: "Tune difficulty, goals, and notification cadence."
    }
};

type Theme = "light" | "dark";

const TABS: { key: TabKey; label: string; icon: string }[] = [
    { key: "learn", label: "Learn", icon: "school" },
    { key: "read", label: "Read", icon: "menu_book" },
    { key: "review", label: "Review", icon: "history" },
    { key: "library", label: "Library", icon: "library_books" },
    { key: "profile", label: "Profile", icon: "person" }
];

const THEME_STORAGE_KEY = "learnancient-theme";

const getInitialTheme = (): Theme => {
    if (typeof window === "undefined") return "light";
    const stored = window.localStorage.getItem(THEME_STORAGE_KEY);
    if (stored === "light" || stored === "dark") return stored;
    const prefersDark = window.matchMedia
        ? window.matchMedia("(prefers-color-scheme: dark)").matches
        : false;
    return prefersDark ? "dark" : "light";
};

export const App: React.FC = () => {
    const [tab, setTab] = useState<TabKey>("read");
    const [theme, setTheme] = useState<Theme>(getInitialTheme);

    useEffect(() => {
        document.documentElement.dataset.theme = theme;
        try {
            window.localStorage.setItem(THEME_STORAGE_KEY, theme);
        } catch {
            // ignore storage errors
        }
    }, [theme]);

    const renderScreen = () => {
        switch (tab) {
            case "learn":
                return <LearnScreen />;
            case "read":
                return <ReadScreen />;
            case "review":
                return <ReviewScreen />;
            case "library":
                return <LibraryScreen />;
            case "profile":
                return <ProfileScreen />;
        }
    };

    return (
        <div className="app-root">
            <div className="app-shell">
                <aside className="nav-rail desktop-only" aria-label="Primary navigation">
                    <div className="nav-logo">ΛA</div>
                    <nav className="nav-rail-inner">
                        {TABS.map(({ key, label, icon }) => (
                            <NavButton
                                key={key}
                                label={label}
                                icon={icon}
                                active={tab === key}
                                onClick={() => setTab(key)}
                            />
                        ))}
                    </nav>
                </aside>

                <main className="main-content">
                    <header className="top-bar">
                        <div className="top-bar-left">
                            <div className="app-title-block">
                                <h1 className="app-title">LearnAncient</h1>
                                <span className="app-subtitle-pill">{TAB_META[tab].label}</span>
                            </div>
                            <p className="top-bar-subtitle">{TAB_META[tab].description}</p>
                        </div>
                        <div className="top-bar-right">
                            <button
                                className="theme-toggle-btn"
                                type="button"
                                aria-label="Toggle light or dark theme"
                                onClick={() => setTheme(theme === "light" ? "dark" : "light")}
                            >
                                <span className="material-icons" aria-hidden="true">
                                    {theme === "light" ? "light_mode" : "dark_mode"}
                                </span>
                            </button>
                            <button className="next-step-btn" type="button">
                                <span className="next-step-label">Next</span>
                                <span className="next-step-dynamic">{NEXT_STEP_LABEL[tab]}</span>
                                <span className="material-icons" aria-hidden="true">
                                    arrow_forward
                                </span>
                            </button>
                        </div>
                    </header>
                    <section className="screen-container">{renderScreen()}</section>
                </main>
            </div>

            <nav className="bottom-tab-bar mobile-only" aria-label="Primary navigation">
                {TABS.map(({ key, label, icon }) => (
                    <TabButton
                        key={key}
                        label={label}
                        icon={icon}
                        active={tab === key}
                        onClick={() => setTab(key)}
                    />
                ))}
            </nav>
        </div>
    );
};

interface NavButtonProps {
    label: string;
    icon?: string;
    active: boolean;
    onClick: () => void;
}

const NavButton: React.FC<NavButtonProps> = ({ label, icon, active, onClick }) => (
    <button
        className={"nav-button" + (active ? " nav-button-active" : "")}
        onClick={onClick}
        type="button"
    >
        {icon && (
            <span className="material-icons nav-button-icon" aria-hidden="true">
                {icon}
            </span>
        )}
        <span className="nav-button-label">{label}</span>
    </button>
);

const TabButton: React.FC<NavButtonProps> = ({ label, icon, active, onClick }) => (
    <button
        className={"tab-button" + (active ? " tab-button-active" : "")}
        onClick={onClick}
        type="button"
    >
        {icon && (
            <span className="material-icons tab-button-icon" aria-hidden="true">
                {icon}
            </span>
        )}
        <span className="tab-button-label">{label}</span>
    </button>
);
