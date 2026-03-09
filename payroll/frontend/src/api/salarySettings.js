import api from "./client";

export async function getSalaryStructures(companyId = null) {
    const params = companyId ? { company_id: companyId } : {};
    const res = await api.get("/salary/salary-structures/", { params });
    // Assuming Django REST paginated response or list
    return res.data?.results || res.data || [];
}

export async function getSalaryComponents(companyId = null) {
    const params = companyId ? { company_id: companyId } : {};
    const res = await api.get("/salary/salary-components/", { params });
    return res.data?.results || res.data || [];
}

export async function getSalaryStructureVersions(structureId = null) {
    const params = structureId ? { salary_structure: structureId } : {};
    const res = await api.get("/salary/salary-structure-versions/", { params });
    return res.data?.results || res.data || [];
}

export async function getComponentMappings(versionId = null) {
    const params = versionId ? { salary_structure_version: versionId } : {};
    const res = await api.get("/salary/salary-structure-component-mappings/", { params });
    return res.data?.results || res.data || [];
}

export async function getPayrollFormulas(companyId = null) {
    const params = companyId ? { company_id: companyId } : {};
    const res = await api.get("/salary/payroll-formulas/", { params });
    return res.data?.results || res.data || [];
}
