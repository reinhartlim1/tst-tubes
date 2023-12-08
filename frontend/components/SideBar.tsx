"use client";
import {
  Box,
  Flex,
  Icon,
  Text,
  Stack,
  VStack,
  BoxProps,
  Drawer,
  DrawerContent,
  IconButton,
  useDisclosure,
  DrawerOverlay,
  useColorModeValue,
  Avatar,
  Button,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  useToast,
} from "@chakra-ui/react";
import { AiOutlineTeam, AiOutlineHome } from "react-icons/ai";
import { BsFolder2 } from "react-icons/bs";
import { FiMenu } from "react-icons/fi";
import { RiFlashlightFill } from "react-icons/ri";
import { useRouter } from "next/navigation";

export default function Sidebar() {
  const { isOpen, onClose, onOpen } = useDisclosure();
  return (
    <Box
      as="section"
      bg={useColorModeValue("gray.50", "gray.700")}
      minH="100vh"
    >
      <SidebarContent display={{ base: "none", md: "unset" }} />
      <Drawer isOpen={isOpen} onClose={onClose} placement="left">
        <DrawerOverlay />
        <DrawerContent>
          <SidebarContent w="full" borderRight="none" />
        </DrawerContent>
      </Drawer>
      <Box ml={{ base: 0, md: 60 }} transition=".3s ease">
        <Flex
          as="header"
          align="center"
          w="full"
          px="4"
          display={{ base: "flex", md: "none" }}
          borderBottomWidth="1px"
          borderColor={useColorModeValue("inherit", "gray.700")}
          bg={useColorModeValue("white", "gray.800")}
          justifyContent={{ base: "space-between", md: "flex-end" }}
          boxShadow="lg"
          h="14"
        >
          <IconButton
            aria-label="Menu"
            display={{ base: "inline-flex", md: "none" }}
            onClick={onOpen}
            icon={<FiMenu />}
            size="md"
          />

          <Flex align="center">
            <Icon as={RiFlashlightFill} h={8} w={8} />
          </Flex>
        </Flex>

        <Box
          as="main"
          p={14}
          minH="30rem"
          bg={useColorModeValue("auto", "gray.800")}
        >
          <Stack
            direction={{ base: "column", sm: "row" }}
            alignItems="center"
            justifyContent="center"
            h="100%"
          ></Stack>
        </Box>
      </Box>
    </Box>
  );
}

const SidebarContent = ({ ...props }: BoxProps) => (
  <Box
    as="nav"
    pos="fixed"
    top="0"
    left="0"
    zIndex="sticky"
    h="full"
    // pb="10"
    overflowX="hidden"
    overflowY="auto"
    bg={useColorModeValue("white", "gray.800")}
    borderColor={useColorModeValue("inherit", "gray.700")}
    borderRightWidth="1px"
    w="60"
    {...props}
  >
    <VStack
      h="full"
      w="full"
      alignItems="flex-start"
      justifyContent="space-between"
    >
      <Box w="full">
        <Flex px="4" py="5" align="center">
          <Icon as={RiFlashlightFill} h={8} w={8} />
          <Text
            fontSize="2xl"
            ml="2"
            color={useColorModeValue("brand.500", "white")}
            fontWeight="semibold"
          >
            TUBESTST
          </Text>
        </Flex>
        <Flex
          direction="column"
          as="nav"
          fontSize="md"
          color="gray.600"
          aria-label="Main Navigation"
        >
          <NavItem icon={AiOutlineHome} path="/dashboard">
            Dashboard
          </NavItem>
          <NavItem icon={AiOutlineTeam} path="/order">
            Order
          </NavItem>
          <NavItem icon={BsFolder2} path="/recommendation">
            Recommendation
          </NavItem>
        </Flex>
      </Box>
      <Flex px="4" py="5" mt={10} justifyContent="center" alignItems="center">
        <Menu>
          <MenuButton
            as={Button}
            size={"sm"}
            rounded={"full"}
            variant={"link"}
            cursor={"pointer"}
            _hover={{ textDecoration: "none" }}
          >
            <Avatar
              size={"sm"}
              name="Ahmad"
              src="https://avatars2.githubusercontent.com/u/37842853?v=4"
            />
          </MenuButton>
          <MenuList fontSize={17} zIndex={5555}>
            <MenuItem
              onClick={() => {
                localStorage.removeItem("token");
                window.location.href = "/signin";
              }}
            >
              Logout
            </MenuItem>
          </MenuList>
        </Menu>
      </Flex>
    </VStack>
  </Box>
);

const NavItem = (props: any) => {
  const color = useColorModeValue("gray.600", "gray.300");
  const router = useRouter();
  const { icon, children, path } = props;
  const handleClick = () => {
    router.push(path);
  };
  return (
    <Flex
      align="center"
      px="4"
      py="3"
      cursor="pointer"
      role="group"
      fontWeight="semibold"
      transition=".15s ease"
      color={useColorModeValue("inherit", "gray.400")}
      _hover={{
        bg: useColorModeValue("gray.100", "gray.900"),
        color: useColorModeValue("gray.900", "gray.200"),
      }}
      onClick={handleClick}
    >
      {icon && (
        <Icon
          mx="2"
          boxSize="4"
          _groupHover={{
            color: color,
          }}
          as={icon}
        />
      )}
      {children}
    </Flex>
  );
};
