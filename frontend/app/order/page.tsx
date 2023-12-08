import OrderForm from "@/components/OrderForm";
import Sidebar from "@/components/SideBar";
import { Flex } from "@chakra-ui/react";

export default function page() {
  return (
    <Flex>
      <Sidebar />
      <OrderForm />
    </Flex>
  );
}
