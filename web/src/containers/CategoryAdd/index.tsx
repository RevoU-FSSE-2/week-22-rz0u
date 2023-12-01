import axios from "axios";
import { CategoryFormAdd } from "../../components";
import { TodosFormAdd as CategoryFormProps } from "../../types";
import { useNavigate } from "react-router-dom";
import { BASE_URL } from "../../environment";
import { useEffect } from "react";

const CategoryAdd = () => {
  const navigate = useNavigate();

  const token = localStorage.getItem("token");
  const headers = {
    Authorization: `Bearer ${token}`,
    "Content-type": "application/json",
  };
  useEffect(() => {
    if (!token) {
      navigate("/login");
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [navigate]);

  const handleSubmit = async (values: CategoryFormProps) => {
    console.log("Todo submitted:", values);
    axios
      .post(`${BASE_URL}/api/todos`, values, {
        headers,
      })
      .then((response) => {
        console.log("Add Successful", response.data);
        navigate("/category");
      });
  };
  return (
    <>
      <CategoryFormAdd onSubmit={handleSubmit} />;
    </>
  );
};
export default CategoryAdd;
