import { useEffect, useState } from "react";
import { GetTodosResponse } from "../../types";
import axios from "axios";
import { CategoryList as CategoryTable } from "../../components";
import { Box, Button, Container, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { BASE_URL } from "../../environment";

const CategoryList = () => {
  const navigate = useNavigate();
  const [info, setInfo] = useState<GetTodosResponse>();

  const handleEditClick = (id: number) => {
    console.log(`Edit clicked for ID: ${id}`);
    navigate(`/category/edit/${id}`);
  };

  const handleDeleteClick = (id: number) => {
    console.log(`Delete clicked for ID: ${id}`);
    axios
      .delete(`${BASE_URL}/api/todos/${id}`, {
        headers,
      })
      .then((response) => {
        console.log(`Resource with ID ${id} has been deleted.`, response);
        setInfo((prevInfo) => {
          if (prevInfo) {
            const updatedInfo = prevInfo.data.filter((item) => item._id !== id);
            return {
              ...prevInfo,
              data: updatedInfo,
            };
          }
          return prevInfo;
        });
      })
      .catch((error) => {
        console.error(`Error deleting resource with ID ${id}:`, error);
      });
  };
  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  const token = localStorage.getItem("token");
  const headers = {
    Authorization: `Bearer ${token}`,
    "Content-type": "application/json",
  };

  const getCategoryList = async () => {
    axios
      .get<GetTodosResponse>(`${BASE_URL}/api/todos`, {
        headers,
      })
      .then((response) => {
        setInfo(response.data);
        console.log(response);
      })
      .catch((error) => {
        console.error("Error fetching API data:", error);
      });
  };

  useEffect(() => {
    getCategoryList();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (!token) {
      navigate("/login");
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [navigate]);

  const filteredData =
    info?.data.map(
      ({
        _id,
        title,
        content,
        priority,
        status,
        dueDates,
        assignor,
        assignee,
        dateCreated,
      }) => ({
        _id,
        title,
        content,
        priority,
        status,
        dueDates,
        assignor,
        assignee,
        dateCreated,
      })
    ) || [];

  return (
    <Container
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        pt: "5rem",
      }}
    >
      <Box>
        <Typography variant="h4" gutterBottom>
          Todos List
        </Typography>
      </Box>
      <Box
        sx={{
          display: "flex",
          marginLeft: "auto",
        }}
      >
        <Button
          variant="outlined"
          sx={{ m: "1rem", mr: "0" }}
          onClick={() => navigate("/category/add")}
        >
          Add
        </Button>
        <Button
          variant="contained"
          color="error"
          sx={{ m: "1rem", mr: "0" }}
          onClick={handleLogout}
        >
          Logout
        </Button>
      </Box>
      <CategoryTable
        data={filteredData}
        onClickEdit={handleEditClick}
        onClickDelete={handleDeleteClick}
      />
    </Container>
  );
};

export default CategoryList;
