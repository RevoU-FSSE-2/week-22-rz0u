import { useNavigate, useParams } from "react-router-dom";
import { CategoryForm } from "../../components";
import { TodosEdit as CategoryFormProps } from "../../types";
import axios from "axios";
import { BASE_URL } from "../../environment";
import { useEffect } from "react";

const CategoryEdit = () => {
  const navigate = useNavigate();

  const { _id } = useParams();
  console.log(_id);

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
    axios
      .put(`${BASE_URL}/api/todos/${_id}`, values, {
        headers,
      })
      .then((response) => {
        console.log("Edit todo submitted:", response.data);
        console.log("Form values submitted:", values);
        navigate("/category");
      })
      .catch((error) => {
        console.log("Error updating:", error);
      });
  };
  return <CategoryForm onSubmit={handleSubmit} />;
};
export default CategoryEdit;
