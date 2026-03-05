import React, { useState, useEffect } from 'react';
import {
    getSalaryStructures,
    getComponentMappings,
    getSalaryComponents
} from '../api/salarySettings';

export default function SalaryStructure() {
    const [activeTab, setActiveTab] = useState('EARNINGS');
    const [structures, setStructures] = useState([]);
    const [mappings, setMappings] = useState([]);
    const [components, setComponents] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchData() {
            try {
                const [stRes, compRes] = await Promise.all([
                    getSalaryStructures(),
                    getSalaryComponents()
                ]);
                setStructures(stRes);
                setComponents(compRes);

                // Fetch mappings if we have a structure (using the first one for now as a demo)
                if (stRes.length > 0) {
                    // Note: We need the active version ID, but we'll fetch all mappings for now 
                    // or handle that logic later stringently 
                    const mapRes = await getComponentMappings();
                    setMappings(mapRes);
                }
            } catch (err) {
                console.error("Failed to load salary data:", err);
            } finally {
                setLoading(false);
            }
        }
        fetchData();
    }, []);

    const activeStructure = structures.length > 0 ? structures[0] : null;

    if (loading) {
        return (
            <div className="glass-panel" style={{ padding: '40px', textAlign: 'center', marginTop: '40px' }}>
                <svg className="spinner" viewBox="0 0 50 50" style={{ width: '40px', height: '40px', animation: 'spin 1s linear infinite', margin: '0 auto 16px', color: 'var(--primary-color)' }}>
                    <circle cx="25" cy="25" r="20" fill="none" stroke="currentColor" strokeWidth="4" strokeDasharray="31.4 31.4" strokeLinecap="round" />
                </svg>
                <p style={{ color: 'var(--text-muted)' }}>Loading Salary Configuration...</p>
                <style jsx>{`@keyframes spin { 100% { transform: rotate(360deg); } }`}</style>
            </div>
        );
    }

    return (
        <div className="animate-fade-in" style={{ paddingBottom: '60px' }}>
            {/* Header Panel */}
            <div className="glass-panel salary-header">
                <div className="header-left">
                    <button className="back-btn">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <line x1="19" y1="12" x2="5" y2="12"></line>
                            <polyline points="12 19 5 12 12 5"></polyline>
                        </svg>
                    </button>
                    <div className="header-title">
                        <h1>{activeStructure ? activeStructure.name : "Executive Salary Structure"}</h1>
                        <p>{activeStructure?.description || "Draft \u2022 Last edited 2 hours ago"}</p>
                    </div>
                </div>
                <div className="header-actions">
                    <button className="btn-secondary">Save Draft</button>
                    <button className="btn-primary" style={{ padding: '8px 20px', width: 'auto' }}>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '8px' }}>
                            <polyline points="20 6 9 17 4 12"></polyline>
                        </svg>
                        Publish Structure
                    </button>
                </div>
            </div>

            {/* Tabs */}
            <div className="tabs-container">
                <button
                    className={`tab-btn ${activeTab === 'EARNINGS' ? 'active' : ''}`}
                    onClick={() => setActiveTab('EARNINGS')}
                >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
                        <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
                    </svg>
                    EARNINGS
                </button>
                <button
                    className={`tab-btn ${activeTab === 'DEDUCTIONS' ? 'active' : ''}`}
                    onClick={() => setActiveTab('DEDUCTIONS')}
                >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10 9 9 9 8 9"></polyline>
                    </svg>
                    DEDUCTIONS
                </button>
                <button
                    className={`tab-btn ${activeTab === 'FORMULA BUILDER' ? 'active' : ''}`}
                    onClick={() => setActiveTab('FORMULA BUILDER')}
                >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <line x1="12" y1="5" x2="12" y2="19"></line>
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                    </svg>
                    FORMULA BUILDER
                </button>
            </div>

            {/* Earnings Components Section */}
            {activeTab === 'EARNINGS' && (
                <>
                    <div className="section-header">
                        <h2 className="section-title">Earnings Components</h2>
                        <button className="add-btn">
                            + Add Component
                        </button>
                    </div>

                    <div className="cards-grid">
                        {/* We map real components from the API matching the appropriate component type */}
                        {components.filter(c => c.component_type === 'EARNING').length > 0 ? (
                            components.filter(c => c.component_type === 'EARNING').map((comp) => {
                                const mapping = mappings.find(m => m.salary_component === comp.id);
                                const isMapped = !!mapping;
                                return (
                                    <div key={comp.id} className="component-card" style={isMapped ? { borderColor: 'var(--primary-color)', backgroundColor: 'var(--bg-glass-hover)', boxShadow: 'var(--shadow-glow)' } : { opacity: comp.is_active ? 1 : 0.7 }}>
                                        <div className="card-content-left">
                                            <div className={`custom-checkbox ${isMapped ? 'checked' : 'disabled'}`}>
                                                {isMapped && (
                                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                                                        <polyline points="20 6 9 17 4 12"></polyline>
                                                    </svg>
                                                )}
                                            </div>
                                            <div className="card-info">
                                                <h3 style={{ color: isMapped ? 'var(--primary-color)' : (comp.is_active ? 'var(--text-main)' : 'var(--text-muted)') }}>{comp.name}</h3>
                                                <p>{mapping ? `${mapping.calculation_type} \u2022 ${mapping.value ? mapping.value : 'Mapped Formula'}` : (comp.is_active ? 'Available' : 'Inactive')}</p>
                                            </div>
                                        </div>
                                        <button className="card-action" style={{ color: isMapped ? 'var(--primary-color)' : 'var(--text-muted)' }}>
                                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                                <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                                                <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                                            </svg>
                                        </button>
                                    </div>
                                );
                            })
                        ) : (
                            <p style={{ color: 'var(--text-muted)' }}>No earning components defined.</p>
                        )}
                    </div>
                </>
            )}

            {/* Formula Builder */}
            {activeTab === 'FORMULA BUILDER' && (
                <div className="formula-builder">
                    <div className="formula-header">
                        <div>
                            <h3 style={{ fontSize: '1.25rem', marginBottom: '4px', color: 'var(--text-main)' }}>Formula Builder</h3>
                            <p style={{ fontSize: '0.875rem' }}>Define how components are calculated</p>
                        </div>
                        <div style={{ display: 'flex', gap: '8px' }}>
                            <span className="badge" style={{ color: 'var(--text-muted)' }}>Condition Engine</span>
                            <span className="badge primary">Active</span>
                        </div>
                    </div>

                    <div className="formula-logic-container">
                        <div className="formula-row">
                            <span className="logic-keyword">IF</span>
                            <span className="logic-variable">Location</span>
                            <span className="logic-keyword">IS</span>
                            <span className="logic-variable">Metro City</span>
                            <span className="logic-keyword">THEN</span>
                            <span className="logic-value-green">50%</span>
                            <span className="logic-keyword">OF</span>
                            <span className="logic-variable-primary">Basic Salary</span>
                        </div>
                        <div className="formula-row">
                            <span className="logic-keyword">ELSE</span>
                            <span className="logic-value-green">40%</span>
                            <span className="logic-keyword">OF</span>
                            <span className="logic-variable-primary">Basic Salary</span>
                        </div>
                    </div>

                    <div className="formula-footer">
                        <button className="btn-ghost">Clear All</button>
                        <button className="btn-dark">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                                <line x1="9" y1="3" x2="9" y2="21"></line>
                            </svg>
                            Apply Formula
                        </button>
                    </div>
                </div>
            )}

            {/* Deduction Components Section */}
            {activeTab === 'DEDUCTIONS' && (
                <>
                    <div className="section-header" style={{ marginTop: '24px' }}>
                        <h2 className="section-title">Deduction Components</h2>
                    </div>

                    <div className="list-layout">
                        {/* We map real components from the API matching the appropriate component type */}
                        {components.filter(c => c.component_type === 'DEDUCTION').length > 0 ? (
                            components.filter(c => c.component_type === 'DEDUCTION').map((comp) => {
                                const mapping = mappings.find(m => m.salary_component === comp.id);
                                const isMapped = !!mapping;

                                return (
                                    <div key={comp.id} className="list-item">
                                        <div className="card-content-left">
                                            <div className={`icon-box ${comp.is_pf_applicable ? 'icon-orange' : (comp.is_esi_applicable ? 'icon-blue' : 'icon-red')}`}>
                                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                                    <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
                                                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
                                                </svg>
                                            </div>
                                            <div className="card-info">
                                                <h3 style={{ color: 'var(--text-main)' }}>{comp.name}</h3>
                                                <p>{mapping ? `${mapping.calculation_type} \u2022 ${mapping.value || 'Formula Based'}` : 'Not mapped to structure'}</p>
                                            </div>
                                        </div>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
                                            {isMapped && <span className="badge" style={{ fontSize: '0.65rem', textTransform: 'uppercase' }}>Configured</span>}
                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--text-muted)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                                <polyline points="9 18 15 12 9 6"></polyline>
                                            </svg>
                                        </div>
                                    </div>
                                );
                            })
                        ) : (
                            <p style={{ color: 'var(--text-muted)' }}>No deduction components configured currently.</p>
                        )}
                    </div>
                </>
            )}
        </div>
    );
}
