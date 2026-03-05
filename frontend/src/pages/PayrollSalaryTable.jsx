import { useEffect, useState } from "react";
import { getPayrollProcessingList } from "../api/payrollProcessing";

export default function PayrollSalaryTable() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        (async () => {
            try {
                const d = await getPayrollProcessingList();
                setData(d);
            } catch (e) {
                setError(e?.response?.data?.detail || "Failed to load payroll data");
            } finally {
                setLoading(false);
            }
        })();
    }, []);

    const formatCurrency = (val) => {
        if (typeof val === 'number') {
            return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(val);
        }
        return val;
    };

    const formatHeader = (key) => {
        return key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    };

    if (loading) return (
        <div className="glass-panel" style={{ padding: '40px', textAlign: 'center' }}>
            <svg className="spinner" viewBox="0 0 50 50" style={{ width: '40px', height: '40px', animation: 'spin 1s linear infinite', margin: '0 auto 16px', color: 'var(--primary-color)' }}>
                <circle cx="25" cy="25" r="20" fill="none" stroke="currentColor" strokeWidth="4" strokeDasharray="31.4 31.4" strokeLinecap="round" />
            </svg>
            <p style={{ color: 'var(--text-muted)' }}>Loading payroll data...</p>
            <style jsx>{`@keyframes spin { 100% { transform: rotate(360deg); } }`}</style>
        </div>
    );

    if (error) return (
        <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid var(--error-color)' }}>
            <h3 style={{ color: 'var(--error-color)', marginBottom: '8px' }}>Error Loading Data</h3>
            <p>{error}</p>
        </div>
    );

    if (data.length === 0) return (
        <div className="glass-panel" style={{ padding: '40px', textAlign: 'center' }}>
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--text-muted)" strokeWidth="1" strokeLinecap="round" strokeLinejoin="round" style={{ marginBottom: '16px' }}>
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
            <h3>No Payroll Records Found</h3>
            <p style={{ color: 'var(--text-muted)' }}>There are currently no salary records to display.</p>
        </div>
    );

    const hiddenColumns = ['id', 'components', 'payroll', 'employee'];
    const headers = Object.keys(data[0]).filter(key => !hiddenColumns.includes(key));

    return (
        <div className="glass-panel" style={{ overflow: 'hidden' }}>
            <div style={{ padding: '24px', borderBottom: '1px solid var(--border-color)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                    <h2 style={{ fontSize: '1.5rem', marginBottom: '4px' }}>Salary Processings</h2>
                    <p style={{ fontSize: '0.875rem' }}>Overview of all employee salary records and deductions.</p>
                </div>
                <div style={{
                    background: 'rgba(99, 102, 241, 0.1)',
                    color: 'var(--primary-color)',
                    padding: '8px 16px',
                    borderRadius: '20px',
                    fontSize: '0.875rem',
                    fontWeight: '600'
                }}>
                    {data.length} Records
                </div>
            </div>

            <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.9rem' }}>
                    <thead>
                        <tr style={{ backgroundColor: 'rgba(255, 255, 255, 0.02)', borderBottom: '1px solid var(--border-color)' }}>
                            {headers.map(key => (
                                <th key={key} style={{ padding: '16px 24px', color: 'var(--text-muted)', fontWeight: '600', whiteSpace: 'nowrap' }}>
                                    {formatHeader(key)}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((row, idx) => (
                            <tr key={idx} className="table-row" style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)', transition: 'background-color 0.2s' }}>
                                {headers.map(key => (
                                    <td key={key} style={{ padding: '16px 24px', whiteSpace: 'nowrap' }}>
                                        <div style={{
                                            display: 'inline-block',
                                            padding: (key === 'status') ? '4px 12px' : '0',
                                            borderRadius: (key === 'status') ? '12px' : '0',
                                            backgroundColor: (key === 'status')
                                                ? (row[key] === 'Paid' || row[key] === 'Completed' ? 'rgba(46, 160, 67, 0.15)' : 'rgba(210, 153, 34, 0.15)')
                                                : 'transparent',
                                            color: (key === 'status')
                                                ? (row[key] === 'Paid' || row[key] === 'Completed' ? '#3fb950' : '#d29922')
                                                : 'inherit',
                                            fontWeight: (key === 'status') ? '600' : 'normal',
                                            fontSize: (key === 'status') ? '0.75rem' : 'inherit',
                                            textTransform: (key === 'status') ? 'uppercase' : 'none',
                                            letterSpacing: (key === 'status') ? '0.05em' : 'normal'
                                        }}>
                                            {typeof row[key] === 'number' && (key.includes('salary') || key.includes('amount') || key.includes('deduction'))
                                                ? formatCurrency(row[key])
                                                : row[key]?.toString() || '-'}
                                        </div>
                                    </td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <style jsx>{`
                .table-row:hover {
                    background-color: rgba(255, 255, 255, 0.03);
                }
            `}</style>
        </div>
    );
}