import { MDBTable, MDBTableBody, MDBTableHead } from "mdb-react-ui-kit";
import type { EmployeeData } from "../types/types";
import EmployeeCard from "./EmployeeCard";

function EmployeeList({ employees }: { employees: EmployeeData[] }) {
  return (
    <MDBTable responsive hover>
      <MDBTableHead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">Email</th>
          <th scope="col">Department</th>
          <th scope="col">Designation</th>
          <th scope="col">Date of Joining</th>
        </tr>
      </MDBTableHead>
      <MDBTableBody>
        {employees.map((employee) => (
          <EmployeeCard key={employee.id} employee={employee} />
        ))}
      </MDBTableBody>
    </MDBTable>
  );
}

export default EmployeeList;
