import type { EmployeeData } from "../types/types";

function EmployeeCard({ employee }: { employee: EmployeeData }) {
  return (
    <tr>
      <th scope="row">{employee.id}</th>
      <td>{employee.name}</td>
      <td>{employee.email}</td>
      <td>{employee.department}</td>
      <td>{employee.designation}</td>
      <td>{employee.date_of_joining}</td>
    </tr>
  );
}

export default EmployeeCard;
