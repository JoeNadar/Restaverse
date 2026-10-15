import { MDBSpinner } from "mdb-react-ui-kit";

function Loader({ message = "Loading employees..." }: { message?: string }) {
  return (
    <div className="d-flex justify-content-center align-items-center gap-2 py-5">
      <MDBSpinner role="status" size="sm" />
      <span>{message}</span>
    </div>
  );
}

export default Loader;
