// import {
//   Table,
//   TableBody,
//   TableCell,
//   TableContainer,
//   TableHead,
//   TableRow,
//   Paper,
//   Button,
//   ButtonGroup,
// } from "@mui/material";
// import { Todos } from "../../types";

// interface Props {
//   data: Todos[];
//   onClickEdit: (_id: string) => void;
//   onClickDelete: (_id: string) => void;
// }

// const [open, setOpen] = React.useState(false);

// const CategoryList = ({ data, onClickEdit, onClickDelete }: Props) => {
//   return (
//     <TableContainer component={Paper} elevation={5}>
//       <Table sx={{ minWidth: 650 }}>
//         <TableHead>
//           <TableRow>
//             <TableCell>Title</TableCell>
//             <TableCell align="center">Assignee</TableCell>
//             <TableCell align="center">Priority</TableCell>
//             <TableCell align="center">Due Date</TableCell>
//             <TableCell align="center">Status</TableCell>
//             <TableCell align="center">Status</TableCell>
//           </TableRow>
//         </TableHead>
//         <TableBody>
//           {data.map((item) => (
//             <TableRow key={item._id}>
//               <TableCell>{item._id}</TableCell>
//               <TableCell align="center">{item.amount}</TableCell>
//               <TableCell align="center">{item.currency}</TableCell>
//               <TableCell align="center">{item.sourceAccount}</TableCell>
//               <TableCell align="center">{item.destinationAccount}</TableCell>
//               <TableCell align="center">{item.status}</TableCell>
//               <TableCell align="center">
//                 <ButtonGroup disableElevation>
//                   <Button
//                     variant="contained"
//                     onClick={() => onClickEdit(item._id)}
//                   >
//                     Approve
//                   </Button>
//                   <Button
//                     variant="outlined"
//                     color="error"
//                     onClick={() => onClickDelete(item._id)}
//                   >
//                     Delete
//                   </Button>
//                 </ButtonGroup>
//               </TableCell>
//             </TableRow>
//           ))}
//         </TableBody>
//       </Table>
//     </TableContainer>
//   );
// };

// export default CategoryList;
