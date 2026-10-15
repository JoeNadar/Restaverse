import workInprogress from "../assets/WorkInProgress.webp";
function NotFound() {
  return (
    <>
      <div className="d-flex justify-content-center">
        <img src={workInprogress} className="w-75 h-100" />
      </div>
    </>
  );
}

export default NotFound;
