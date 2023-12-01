export interface LoginForm {
  username: string;
  password: string;
}

export interface LoginResponse {
  data: {
    token: string;
  };
}

export interface RegisterForm {
  email: string;
  username: string;
  password: string;
  role: string;
}

export interface RegisterResponse {
  data: {
    email: string;
    username: string;
    password: string;
    role: string;
  };
}

export interface Todos {
  _id: number;
  title: string;
  content: string;
  priority: string;
  status: string;
  dueDates: string;
  assignor: string;
  assignee: string;
  dateCreated: string;
}

export interface GetTodosResponse {
  data: Todos[];
  current_page: number;
  total_item: number;
  total_page: number;
}

export type TodosForm = Omit<Todos, "_id">;

export type TodosFormAdd = Omit<
  Todos,
  "_id" | "status" | "assignor" | "dateCreated"
>;

export interface TodosEdit {
  _id: number;
  status: string;
}
