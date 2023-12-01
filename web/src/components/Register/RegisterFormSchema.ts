import * as Yup from "yup";

export const initialValues = {
  email: "",
  username: "",
  password: "",
  role: "employee",
};

export const validationSchema = Yup.object({
  email: Yup.string()
    .email("Invalid Email Address")
    .required("Please fill in your Email Address"),
  username: Yup.string().required("Please fill in your Username"),
  password: Yup.string()
    .matches(
      /^(?=.*[A-Za-z])(?=.*\d).{5,}$/,
      "Password must contain at least one alphabet and one number, and be at least 5 characters long."
    )
    .required("Please fill in your desired Password"),
  role: Yup.string().required("Please pick your Role"),
});
