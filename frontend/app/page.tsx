import { Container, Stack, HStack, VStack, Flex, Text, Image, Box, Button, Link } from '@chakra-ui/react';

export default function Home() {
  const overviewList = [
    { id: 1, label: 'Login or Signup', subLabel: 'The process should be quick.' },
    {
      id: 2,
      label: 'Create your order',
      subLabel: 'You can choose the product you want to order'
    },
    {
      id: 3,
      label: 'See your recipe recommendation',
      subLabel: 'You can see the recommended recipe based on your order and product.'
    },
    {
      id: 4,
      label: 'Sign Out',
      subLabel: 'You can sign out if you want to exit the application.'
    }
  ];
  return (
    <Container maxW="6xl" py={10}>
      <Text fontSize="4xl" fontWeight="bold" textAlign="center" mb={2}>
        TUBES TST 101
      </Text>
      <Stack
        direction={{ base: 'column', md: 'row' }}
        spacing={{ base: 0, md: 3 }}
        justifyContent="center"
        alignItems="center"
      >
        <VStack spacing={4} alignItems="flex-start" mb={{ base: 5, md: 0 }} maxW="md">
          {overviewList.map((data) => (
            <Box key={data.id}>
              <HStack spacing={2}>
                <Flex
                  fontWeight="bold"
                  boxShadow="md"
                  color="white"
                  bg="blue.400"
                  rounded="full"
                  justifyContent="center"
                  alignItems="center"
                  w={10}
                  h={10}
                >
                  {data.id}
                </Flex>
                <Text fontSize="xl">{data.label}</Text>
              </HStack>
              <Text fontSize="md" color="gray.500" ml={12}>
                {data.subLabel}
              </Text>
            </Box>
          ))}
        </VStack>
      </Stack>
      <Flex justifyContent="center" pt={5}>
        <Button
          as={Link}
          href="/signin"
          color="white"
          variant="solid"
          size="lg"
          rounded="md"
          mb={{ base: 2, sm: 0 }}
          lineHeight={1}
          bgGradient="linear(to-l, #0ea5e9,#2563eb)"
          _hover={{ bgGradient: 'linear(to-l, #0ea5e9,#2563eb)' }}
        >
          Get Started
        </Button>
      </Flex>
    </Container>
  );
};

