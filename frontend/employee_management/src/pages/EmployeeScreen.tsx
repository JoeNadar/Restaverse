import { useState } from "react";
import { MDBContainer, MDBSpinner } from "mdb-react-ui-kit";
import SearchBar from "../components/SearchBar";
import EmployeeList from "../components/EmployeeList";
import Pagination from "../components/Pagination";
import Loader from "../components/Loader";
import ErrorMessage from "../components/ErrorMessage";
import { useDebounce } from "../hooks/debouncer-hook";
import { useEmployees } from "../hooks/use-employees";

const PAGE_SIZE = 10;
const SEARCH_DELAY_MS = 1000;

function EmployeeScreen() {
  const [query, setQuery] = useState("");
  const [page, setPage] = useState(1);

  // Only send the search after the user stops typing for 500ms,
  // so typing "Rah" makes 1 request instead of 3
  const search = useDebounce(query, SEARCH_DELAY_MS).trim();

  // When the search changes, go back to page 1.
  const [lastSearch, setLastSearch] = useState(search);
  if (search !== lastSearch) {
    setLastSearch(search);
    setPage(1);
  }

  const { data, isLoading, error, retry } = useEmployees({
    search,
    page,
    size: PAGE_SIZE,
  });

  function renderResults() {
    if (error) {
      return <ErrorMessage message={error} onRetry={retry} />;
    }

    // First load: nothing to show yet
    if (!data) {
      return <Loader />;
    }

    if (data.items.length === 0) {
      return (
        <p className="text-center text-muted py-5">
          {search
            ? `No employees found matching "${search}".`
            : "No employees found."}
        </p>
      );
    }

    const firstItem = (data.page - 1) * data.size + 1;
    const lastItem = firstItem + data.items.length - 1;

    return (
      <>
        <div className="d-flex align-items-center gap-2 mb-2 text-muted">
          <span>
            Showing {firstItem}–{lastItem} of {data.total} employees
          </span>
          {/* Small spinner while new results load; old results stay visible */}
          {isLoading && <MDBSpinner size="sm" role="status" />}
        </div>
        <div style={{ opacity: isLoading ? 0.6 : 1 }}>
          <EmployeeList employees={data.items} />
        </div>
        <Pagination
          page={data.page}
          totalPages={data.pages}
          onPageChange={setPage}
          disabled={isLoading}
        />
      </>
    );
  }

  return (
    <MDBContainer className="py-5">
      <h1 className="h3 mb-4">Employee Directory</h1>
      <div className="mb-4">
        <SearchBar value={query} onChange={setQuery} />
      </div>
      {/* aria-live lets screen readers announce result changes */}
      <div aria-live="polite">{renderResults()}</div>
    </MDBContainer>
  );
}

export default EmployeeScreen;
