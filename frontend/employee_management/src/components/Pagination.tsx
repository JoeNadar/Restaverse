import { MDBBtn } from "mdb-react-ui-kit";
import type { PaginationProps } from "../types/types";

function Pagination({
  page,
  totalPages,
  onPageChange,
  disabled = false,
}: PaginationProps) {
  // No need for buttons when everything fits on one page
  if (totalPages <= 1) return null;

  return (
    <div className="d-flex justify-content-center align-items-center gap-3">
      <MDBBtn
        color="light"
        disabled={disabled || page <= 1}
        onClick={() => onPageChange(page - 1)}
      >
        Previous
      </MDBBtn>
      <span>
        Page {page} of {totalPages}
      </span>
      <MDBBtn
        color="light"
        disabled={disabled || page >= totalPages}
        onClick={() => onPageChange(page + 1)}
      >
        Next
      </MDBBtn>
    </div>
  );
}

export default Pagination;
