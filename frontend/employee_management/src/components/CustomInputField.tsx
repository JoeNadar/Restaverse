import { MDBInput } from "mdb-react-ui-kit";
import type { CustomInputComponentProps } from "../types/types";

// A generic controlled text input. It only shows the value and reports changes;
// the parent decides what to do with them.
function CustomInputField({
  value,
  onChange,
  label,
  placeholder,
}: CustomInputComponentProps) {
  return (
    <MDBInput
      value={value}
      onChange={(e) => onChange(e.target.value)}
      label={label}
      placeholder={placeholder}
      type="text"
    />
  );
}

export default CustomInputField;
