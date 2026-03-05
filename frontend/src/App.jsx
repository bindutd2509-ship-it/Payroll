import { useState } from "react";
import Login from "./pages/Login";
import SalaryStructure from "./pages/SalaryStructure";
import "./index.css";
import "./App.css";

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(
    !!localStorage.getItem("accessToken")
  );

  function logout() {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    setIsLoggedIn(false);
  }

  return (
    <div className="app-wrapper">
      <header className="app-header glass-panel">
        <div className="container header-content">
          <div className="brand">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--primary-color)', marginRight: '10px' }}>
              <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
              <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
            </svg>
            <h2>Payroll Pro</h2>
          </div>
          {isLoggedIn && (
            <button className="btn-secondary" onClick={logout}>
              Sign Out
            </button>
          )}
        </div>
      </header>

      <main className="main-content container animate-fade-in">
        {isLoggedIn ? (
          <SalaryStructure />
        ) : (
          <Login onLogin={() => setIsLoggedIn(true)} />
        )}
      </main>
    </div>
  );
}