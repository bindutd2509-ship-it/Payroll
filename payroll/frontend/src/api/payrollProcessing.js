import api from "./client";

export async function getPayrollProcessingList() {
    const res = await api.get("/payroll-processing/items/");
    return Array.isArray(res.data) ? res.data : [];
}