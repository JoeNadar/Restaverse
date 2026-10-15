export type CustomInputComponentProps = {
  value: string;
  onChange: (value: string) => void;
  label: string;
  placeholder?: string;
};

export type SearchBarProps = {
  value: string;
  onChange: (value: string) => void;
};

export type PaginationProps = {
  page: number;
  totalPages: number;
  onPageChange: (page: number) => void;
  disabled?: boolean;
};

export type GetEmployeesParams = {
  page?: number;
  size?: number;
  search?: string;
  signal?: AbortSignal;
};

export type EmployeeData = {
  id: number;
  name: string;
  email: string;
  department: string;
  designation: string;
  date_of_joining: string;
};

export type PaginatedResponse<T> = {
  total: number;
  page: number;
  size: number;
  pages: number;
  items: T[];
};
