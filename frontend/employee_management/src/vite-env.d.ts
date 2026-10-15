/// <reference types="vite/client" />

// Tells TypeScript which env variables we expect (all must start with VITE_)
interface ImportMetaEnv {
  readonly VITE_BASE_API_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
