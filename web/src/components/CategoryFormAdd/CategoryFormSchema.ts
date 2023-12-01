import * as Yup from "yup";

export const initialValues = {
  title: "",
  content: "",
  priority: "low",
  dueDates: "",
  assignee: "",
};

export const validationSchema = Yup.object({
  title: Yup.string().required("Please fill in the title"),
  content: Yup.string().required("Please fill in the content"),
  priority: Yup.string().required("Please fill in the priority"),
  dueDates: Yup.date().required("Please fill in the deadline"),
  assignee: Yup.string().required("Please fill in the person in charge"),
});
