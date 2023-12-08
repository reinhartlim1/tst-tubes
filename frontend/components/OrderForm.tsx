"use client";
import {
  Container,
  Box,
  Heading,
  Flex,
  FormControl,
  FormLabel,
  Select,
  NumberInput,
  NumberInputField,
  NumberInputStepper,
  NumberIncrementStepper,
  NumberDecrementStepper,
  useToast,
  Stack,
  Button,
} from "@chakra-ui/react";
import { useState, useEffect } from "react";
import http from "../app/axios";
import { useRouter } from "next/navigation";

export default function OrderForm() {
  const router = useRouter();
  const toast = useToast();
  const [product, setProduct] = useState(0);
  const [quantity, setQuantity] = useState(0);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await http.get("/product/", {
          headers: {
            "Authorization": "Bearer " + localStorage.getItem("token"),
          },
        });
        setProducts(response.data);
      } catch (error) {
        console.error("Fetch products failed:", error);
      }
    };
    fetchProducts();
  }, []);

  const handleOrder = async () => {
    try {
      const response = await http.post(
        "/orders/",
        {
          product_id: product,
          quantity: quantity,
        },
        {
          headers: {
            "Authorization": "Bearer " + localStorage.getItem("token"),
            "Content-Type": "application/json",
          },
        }
      );
      toast({
        title: "Order success",
        description: "Thank you for your order",
        status: "success",
        duration: 9000,
        isClosable: true,
        position: "top",
      });
      router.push("/dashboard");
    } catch (error) {
      console.error("Order failed:", error);
      toast({
        title: "Order failed",
        description: "Check your input",
        status: "error",
        duration: 9000,
        isClosable: true,
        position: "top",
      });
    }
  };
  return (
    <Container maxW="5xl" p={{ base: 5, md: 10 }}>
      <Heading as="h3" size="lg" mb="4" fontWeight="bold" textAlign="left">
        Order
      </Heading>
      <Box as="form" mb={{ base: "2.5rem", lg: "4rem" }}>
        <Flex
          justifyContent="start"
          alignItems="start"
          flexDirection={{ base: "column", lg: "row" }}
        >
          <FormControl
            id="where"
            width={{ base: "100%", lg: 1 / 3 }}
            pr={{ lg: "2" }}
            mb={{ base: "4", lg: "0" }}
          >
            <FormLabel fontSize="0.75rem" fontWeight="bold">
              Quantity
            </FormLabel>
            <NumberInput
              min={1}
              value={quantity}
              onChange={(quantity) => setQuantity(parseInt(quantity))}
            >
              <NumberInputField />
              <NumberInputStepper>
                <NumberIncrementStepper />
                <NumberDecrementStepper />
              </NumberInputStepper>
            </NumberInput>
          </FormControl>
          <FormControl
            id="product"
            width={{ base: "100%", lg: 1 / 3 }}
            pr={{ lg: "2" }}
            mb={{ base: "4", lg: "0" }}
          >
            <FormLabel fontSize="0.75rem" fontWeight="bold">
              Product
            </FormLabel>
            <Select
              value={product}
              onChange={(e) => setProduct(parseInt(e.target.value))}
            >
              {products?.map((product: any) => (
                <option key={product.product_id} value={product.product_id}>
                  {product.product_id} - {product.product_name}
                </option>
              ))}
            </Select>
          </FormControl>
          <Stack spacing={10}>
              <Stack
                direction={{ base: "column", sm: "row" }}
                align={"start"}
                justify={"space-between"}
              ></Stack>
              <Button
                bg={"blue.400"}
                color={"white"}
                _hover={{
                  bg: "blue.500",
                }}
                onClick={handleOrder}
              >
                Order
              </Button>
            </Stack>
        </Flex>
      </Box>
    </Container>
  );
}
