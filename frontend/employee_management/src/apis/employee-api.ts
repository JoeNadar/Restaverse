import type {
  EmployeeData,
  GetEmployeesParams,
  PaginatedResponse,
} from "../types/types";
import { api } from "./client";

export async function getEmployees({
  page = 1,
  size = 10,
  search,
  signal,
}: GetEmployeesParams = {}): Promise<PaginatedResponse<EmployeeData>> {
  // The backend returns 400 for an empty search, so we leave it out instead
  const trimmedSearch = search?.trim();

  const response = await api.get<PaginatedResponse<EmployeeData>>(
    "/employees",
    {
      params: { page, size, search: trimmedSearch || undefined },
      signal,
    }
  );
  return response.data;
}
