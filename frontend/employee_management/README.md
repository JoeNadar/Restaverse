# Employee Directory – Frontend

React + Vite + TypeScript app to search employees by name or department.
UI components come from [MDB React UI Kit](https://mdbootstrap.com/docs/react/).

## How to run

1. Install packages
   ```
   cd .\employee_management\
   ```
   ```
   npm install
   ```
   (`.npmrc` sets `legacy-peer-deps=true` because `mdb-react-ui-kit` uses
   `framer-motion@10`, which only lists React 18 as a peer. It works fine on React 19.)
2. Create a `.env` file (see `.env.example`)
   ```
   VITE_BASE_API_URL=http://127.0.0.1:8000
   ```
3. Start the dev server
   ```
   npm run dev
   ```
4. Open http://localhost:5173 (the backend must be running too).

## How search performance is optimized (conceptually)

When a user is typing making API call for every letter is not optimal and irrelevant until the user finishes typing after the user finishes the typing is the time we need to make the API call because the user would have completed typing what he want to search so We use debouncer in search which lets you make the API call after the User finishes typing and after a certain time the API call is made which makes it Optimal
