import { Route, Routes } from "react-router";
import EmployeeScreen from "./pages/EmployeeScreen";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <>
      {/* we can use another file routes and add it here for more complex apps  */}
      <Routes>
        <Route index element={<EmployeeScreen />}></Route>
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </>
  );
}

export default App;
