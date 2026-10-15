import axios from "axios";

type FastApiErrorBody = {
  detail?: string | { msg: string }[];
};

export function getErrorMessage(error: unknown): string {
  if (!axios.isAxiosError<FastApiErrorBody>(error)) {
    return "Something went wrong. Please try again.";
  }

  if (error.code === "ECONNABORTED") {
    return "The server took too long to respond. Please try again.";
  }

  // No response means the server is down or there is no internet
  if (!error.response) {
    return "Could not reach the server. Please check your connection and try again.";
  }

  const detail = error.response.data?.detail;
  if (typeof detail === "string") {
    return detail;
  }
  if (Array.isArray(detail) && detail.length > 0) {
    return detail.map((item) => item.msg).join(", ");
  }

  return `Request failed with status ${error.response.status}. Please try again.`;
}
