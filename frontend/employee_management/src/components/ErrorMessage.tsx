import { MDBBtn } from "mdb-react-ui-kit";

type ErrorMessageProps = {
  message: string;
  onRetry?: () => void;
};

function ErrorMessage({ message, onRetry }: ErrorMessageProps) {
  return (
    <div
      className="alert alert-danger d-flex justify-content-between align-items-center"
      role="alert"
    >
      <span>
        <strong>Could not load employees.</strong> {message}
      </span>
      {onRetry && (
        <MDBBtn color="danger" size="sm" onClick={onRetry}>
          Try again
        </MDBBtn>
      )}
    </div>
  );
}

export default ErrorMessage;
