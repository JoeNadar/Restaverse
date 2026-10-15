import type { SearchBarProps } from "../types/types";
import CustomInputField from "./CustomInputField";

function SearchBar({ value, onChange }: SearchBarProps) {
  return (
    <CustomInputField
      value={value}
      onChange={onChange}
      label="Search employees"
      placeholder="Search by name or department"
    />
  );
}

export default SearchBar;
