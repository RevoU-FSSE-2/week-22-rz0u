import * as Yup from "yup";

export const initialValues = {
  status: "not completed",
  _id: 0,
};

export const validationSchema = Yup.object({
  status: Yup.string().required("Please fill in the progression"),
});
