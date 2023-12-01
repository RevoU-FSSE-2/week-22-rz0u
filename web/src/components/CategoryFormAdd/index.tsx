import { useFormik } from "formik";
import {
  Box,
  Button,
  Container,
  FormControl,
  FormHelperText,
  IconButton,
  InputLabel,
  MenuItem,
  Paper,
  Select,
  TextField,
  Typography,
} from "@mui/material";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import { Todos, TodosFormAdd as TodosFormProps } from "../../types";
import { initialValues, validationSchema } from "./CategoryFormSchema";
import { useNavigate } from "react-router-dom";
import { blue } from "@mui/material/colors";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { MobileDatePicker } from "@mui/x-date-pickers/MobileDatePicker";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";

interface Props {
  onSubmit: (values: TodosFormProps) => void;
  category?: Todos;
}

const CategoryFormAdd = ({ onSubmit, category }: Props) => {
  const handleSubmit = (values: TodosFormProps) => {
    onSubmit(values);
  };
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: category ?? initialValues,
    onSubmit: handleSubmit,
    validationSchema: validationSchema,
  });

  return (
    <Container
      sx={{
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center",
        pt: "5rem",
      }}
    >
      <Paper
        elevation={5}
        sx={{
          maxWidth: "max-content",
          padding: "1rem",
          margin: "3rem",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Typography variant="h6" sx={{ m: "1rem" }}>
          ADD TODOS
        </Typography>
        <Button variant="text" onClick={() => navigate("/category")}>
          Back
        </Button>
        <form onSubmit={formik.handleSubmit}>
          <Box sx={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
            <TextField
              name="title"
              label="Title"
              value={formik.values.title}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              error={formik.touched.title && Boolean(formik.errors.title)}
              helperText={formik.touched.title && formik.errors.title}
              size="small"
            />
            <TextField
              name="content"
              label="Content"
              value={formik.values.content}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              error={formik.touched.content && Boolean(formik.errors.content)}
              helperText={formik.touched.content && formik.errors.content}
              size="small"
            />
            <FormControl fullWidth>
              <InputLabel>Priority</InputLabel>
              <Select
                name="priority"
                label="Priority"
                defaultValue={"low"}
                value={formik.values.priority}
                onChange={formik.handleChange}
                error={
                  formik.touched.priority && Boolean(formik.errors.priority)
                }
                size="small"
              >
                <MenuItem value={"high"}>High</MenuItem>
                <MenuItem value={"medium"}>Medium</MenuItem>
                <MenuItem value={"low"}>Low</MenuItem>
                {formik.touched.priority && formik.errors.priority && (
                  <FormHelperText error>
                    {formik.errors.priority}
                  </FormHelperText>
                )}
              </Select>
            </FormControl>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <MobileDatePicker
                label="Due Date"
                value={formik.values.dueDates}
                onChange={(date) => formik.setFieldValue("dueDates", date)}
              />
            </LocalizationProvider>
            <TextField
              name="assignee"
              label="Assignee"
              value={formik.values.assignee}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              error={formik.touched.assignee && Boolean(formik.errors.assignee)}
              helperText={formik.touched.assignee && formik.errors.assignee}
              size="small"
            />
            <IconButton type="submit" disableRipple>
              <AddCircleOutlineIcon sx={{ color: blue[400] }} />
            </IconButton>
          </Box>
        </form>
      </Paper>
    </Container>
  );
};

export default CategoryFormAdd;
