import axios from "axios";
import { RegisterForm } from "../../components";
import { RegisterForm as RegisterFormProps } from "../../types";
import { BASE_URL } from "../../environment";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const navigate = useNavigate();
  const onSubmit = async (values: RegisterFormProps) => {
    axios
      .post(`${BASE_URL}/api/users/register`, {
        email: values.email,
        username: values.username,
        role: values.role,
        password: values.password,
      })
      .then((response) => {
        console.log("Register successful", response.data);
        navigate("/login");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return <RegisterForm onSubmit={onSubmit} />;
};

export default Register;
