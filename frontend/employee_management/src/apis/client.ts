import axios from "axios";

const baseURL = import.meta.env.VITE_BASE_API_URL;

// Fail early with a clear message instead of sending requests to the wrong place
if (!baseURL) {
  throw new Error(
    "VITE_BASE_API_URL is not set. Copy .env.example to .env and set the backend URL."
  );
}

// One shared axios instance for the whole app
export const api = axios.create({
  baseURL,
  timeout: 10000, // give up after 10 seconds
});
