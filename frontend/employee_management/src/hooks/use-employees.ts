import { useEffect, useState } from "react";
import axios from "axios";
import { getEmployees } from "../apis/employee-api";
import { getErrorMessage } from "../apis/api-error";
import type { EmployeeData, PaginatedResponse } from "../types/types";

type UseEmployeesParams = {
  search: string;
  page: number;
  size: number;
};

// Keeps all the API logic out of the UI components.
// The page just tells us what to search and gets back data / loading / error.
export function useEmployees({ search, page, size }: UseEmployeesParams) {
  const [data, setData] = useState<PaginatedResponse<EmployeeData> | null>(
    null
  );
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  // Changing this number makes the effect run again (used by the Retry button)
  const [retryCount, setRetryCount] = useState(0);

  useEffect(() => {
    // If search/page changes before this request finishes, we cancel it
    // so an old response can never overwrite a newer one
    const controller = new AbortController();

    async function load() {
      setIsLoading(true);
      setError(null);
      try {
        const result = await getEmployees({
          search,
          page,
          size,
          signal: controller.signal,
        });
        setData(result);
        setIsLoading(false);
      } catch (err) {
        // A cancelled request is expected, not an error to show
        if (axios.isCancel(err)) return;
        setError(getErrorMessage(err));
        setIsLoading(false);
      }
    }

    load();
    return () => controller.abort();
  }, [search, page, size, retryCount]);

  function retry() {
    setRetryCount((count) => count + 1);
  }

  return { data, isLoading, error, retry };
}
