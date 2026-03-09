import { useState } from "react";
import api from "../api/client";

export default function Login({ onLogin }) {
    const [email, setEmail] = useState("admin@gmail.com");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleSubmit(e) {
        e.preventDefault();
        setError("");
        setLoading(true);

        try {
            // BACKEND EXPECTS email + password
            const res = await api.post("/token/", {
                email: email,
                password: password,
            });

            localStorage.setItem("accessToken", res.data.access);
            localStorage.setItem("refreshToken", res.data.refresh);

            onLogin && onLogin();
        } catch (err) {
            setError(
                err?.response?.data?.detail ||
                err?.response?.data?.email?.[0] ||
                "Invalid credentials. Please try again."
            );
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="login-container" style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            minHeight: '70vh'
        }}>
            <div className="glass-panel" style={{
                width: '100%',
                maxWidth: '420px',
                padding: '40px',
                textAlign: 'center'
            }}>
                <div style={{ marginBottom: '32px' }}>
                    <h2 style={{ fontSize: '1.75rem', marginBottom: '8px', color: '#fff' }}>Welcome Back</h2>
                    <p>Enter your credentials to access the payroll system</p>
                </div>

                <form onSubmit={handleSubmit} style={{ textAlign: 'left' }}>
                    <div style={{ marginBottom: '20px' }}>
                        <label className="input-label">Email Address</label>
                        <input
                            type="email"
                            className="input-field"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="admin@gmail.com"
                            required
                        />
                    </div>

                    <div style={{ marginBottom: '24px' }}>
                        <label className="input-label">Password</label>
                        <input
                            type="password"
                            className="input-field"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="••••••••"
                            required
                        />
                    </div>

                    {error && (
                        <div style={{
                            padding: '12px',
                            backgroundColor: 'rgba(248, 81, 73, 0.1)',
                            border: '1px solid rgba(248, 81, 73, 0.4)',
                            borderRadius: '8px',
                            color: 'var(--error-color)',
                            fontSize: '0.875rem',
                            marginBottom: '20px',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '8px'
                        }}>
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                            {error}
                        </div>
                    )}

                    <button type="submit" className="btn-primary" disabled={loading}>
                        {loading ? (
                            <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <svg className="spinner" viewBox="0 0 50 50" style={{ width: '20px', height: '20px', animation: 'spin 1s linear infinite' }}>
                                    <circle cx="25" cy="25" r="20" fill="none" stroke="currentColor" strokeWidth="4" strokeDasharray="31.4 31.4" strokeLinecap="round" />
                                </svg>
                                Authenticating...
                            </span>
                        ) : "Sign In"}
                    </button>
                </form>
            </div>

            <style jsx>{`
                @keyframes spin { 100% { transform: rotate(360deg); } }
            `}</style>
        </div>
    );
}