import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Button,
  ButtonGroup,
} from "@mui/material";
import { Todos } from "../../types";

interface Props {
  data: Todos[];
  onClickEdit: (_id: number) => void;
  onClickDelete: (_id: number) => void;
}

const CategoryList = ({ data, onClickEdit, onClickDelete }: Props) => {
  return (
    <TableContainer component={Paper} elevation={5}>
      <Table sx={{ minWidth: 650 }}>
        <TableHead>
          <TableRow>
            <TableCell>Title</TableCell>
            <TableCell align="center">Content</TableCell>
            <TableCell align="center">Priority</TableCell>
            <TableCell align="center">Status</TableCell>
            <TableCell align="center">Due Date</TableCell>
            <TableCell align="center">Assignor</TableCell>
            <TableCell align="center">Assignee</TableCell>
            <TableCell align="center">Date Created</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((item) => (
            <TableRow key={item._id}>
              <TableCell>{item.title}</TableCell>
              <TableCell align="center">{item.content}</TableCell>
              <TableCell align="center">{item.priority}</TableCell>
              <TableCell align="center">{item.status}</TableCell>
              <TableCell align="center">{item.dueDates}</TableCell>
              <TableCell align="center">{item.assignor}</TableCell>
              <TableCell align="center">{item.assignee}</TableCell>
              <TableCell align="center">{item.dateCreated}</TableCell>
              <TableCell align="center">
                <ButtonGroup disableElevation>
                  <Button
                    variant="contained"
                    onClick={() => onClickEdit(item._id)}
                  >
                    Edit
                  </Button>
                  <Button
                    variant="outlined"
                    color="error"
                    onClick={() => onClickDelete(item._id)}
                  >
                    Delete
                  </Button>
                </ButtonGroup>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default CategoryList;
