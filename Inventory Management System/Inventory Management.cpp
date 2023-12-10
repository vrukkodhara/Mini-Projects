#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>

class ProductBase {
protected:
    int id;
    std::string name;
    double price;

public:
    ProductBase(int _id, const std::string& _name, double _price)
        : id(_id), name(_name), price(_price) {}

    int getID() const { return id; }
    std::string getName() const { return name; }
    double getPrice() const { return price; }

    virtual void display() const = 0;
    virtual void updateQuantity(int newQuantity) = 0;
    virtual std::string getType() const = 0;
    virtual ~ProductBase() = default;
};

class PhysicalProduct : public ProductBase {
private:
    int quantity;

public:
    PhysicalProduct(int _id, const std::string& _name, double _price, int _quantity)
        : ProductBase(_id, _name, _price), quantity(_quantity) {}

    int getQuantity() const { return quantity; }

    void display() const override {
        std::cout << std::setw(5) << id << std::setw(20) << name << std::setw(10) << price
                  << std::setw(10) << quantity << " units\n";
    }

    void updateQuantity(int newQuantity) override {
        quantity = newQuantity;
    }

    std::string getType() const override {
        return "Physical Product";
    }
};

class DigitalProduct : public ProductBase {
private:
    std::string format;

public:
    DigitalProduct(int _id, const std::string& _name, double _price, const std::string& _format)
        : ProductBase(_id, _name, _price), format(_format) {}

    void display() const override {
        std::cout << std::setw(5) << id << std::setw(20) << name << std::setw(10) << price
                  << std::setw(20) << format << " format\n";
    }

    void updateQuantity(int newQuantity) override {
        // For digital products, quantity is not applicable
    }

    std::string getType() const override {
        return "Digital Product";
    }
};

class Customer {
private:
    std::string name;
    int customerId;

public:
    Customer(const std::string& _name, int _customerId)
        : name(_name), customerId(_customerId) {}

    std::string getName() const { return name; }
    int getCustomerId() const { return customerId; }
};

class Inventory {
private:
    std::vector<ProductBase*> products;
    std::vector<Customer> customers;

public:
    ~Inventory() {
        for (auto& product : products) {
            delete product;
        }
    }

    void addProduct(ProductBase* product) {
        products.push_back(product);
    }

   void displayInventory() const {
    std::cout << "ID   Name                 Price     Quantity" << std::endl;

    if (products.empty()) {
        std::cout << "Nothing in the inventory." << std::endl;
    } else {
        for (const auto& product : products) {
            product->display();
        }
    }
}


    ProductBase* findProduct(int productId) {
        for (auto& product : products) {
            if (product->getID() == productId) {
                return product;
            }
        }
        return nullptr;
    }

    void updateProductQuantity(int productId, int newQuantity) {
        ProductBase* product = findProduct(productId);
        if (product) {
            product->updateQuantity(newQuantity);
            std::cout << "Quantity updated successfully!" << std::endl;
        } else {
            std::cout << "Product not found!" << std::endl;
        }
    }

    void addCustomer(const Customer& customer) {
        customers.push_back(customer);
    }

    void displayCustomers() const {
        std::cout << "Customer ID   Name\n";
        for (const auto& customer : customers) {
            std::cout << std::setw(12) << customer.getCustomerId() << std::setw(20) << customer.getName() << std::endl;
        }
    }

    void saveToFile(const std::string& filename) const {
        std::ofstream outFile(filename);
        for (const auto& product : products) {
            outFile << product->getType() << "," << product->getID() << ","
                    << product->getName() << "," << product->getPrice() << ",";
            if (auto physicalProduct = dynamic_cast<PhysicalProduct*>(product)) {
                outFile << physicalProduct->getQuantity();
            } else if (auto digitalProduct = dynamic_cast<DigitalProduct*>(product)) {
                outFile << digitalProduct->getType();
            }
            outFile << "\n";
        }
        outFile.close();
    }

    void loadFromFile(const std::string& filename) {
        std::ifstream inFile(filename);
        if (!inFile.is_open()) {
            std::cerr << "Error opening file!" << std::endl;
            return;
        }

        std::string type;
        int id;
        std::string name;
        double price;
        int quantity;
        std::string format;

        while (inFile >> std::quoted(type) >> id >> std::quoted(name) >> price) {
            if (type == "Physical Product") {
                inFile >> quantity;
                PhysicalProduct* product = new PhysicalProduct(id, name, price, quantity);
                addProduct(product);
            } else if (type == "Digital Product") {
                inFile >> std::quoted(format);
                DigitalProduct* product = new DigitalProduct(id, name, price, format);
                addProduct(product);
            }
        }

        inFile.close();
    }
};

void showMenu() {
    std::cout << "1. Add Product\n"
              << "2. Display Inventory\n"
              << "3. Update Product Quantity\n"
              << "4. Save Inventory to File\n"
              << "5. Load Inventory from File\n"
              << "6. Add Customer\n"
              << "7. Display Customers\n"
              << "8. Exit\n"
              << "Enter your choice: ";
}

int main() {
    Inventory inventory;

    while (true) {
        showMenu();
        int choice;
        std::cin >> choice;

        switch (choice) {
            case 1: {
                int id, quantity;
                double price;
                std::string name, type, format;

                std::cout << "Enter product details:" << std::endl;
                std::cout << "ID: ";
                std::cin >> id;

                std::cout << "Name: ";
                std::cin.ignore();  // clear the newline character from the buffer
                std::getline(std::cin, name);

                std::cout << "Price: ";
                std::cin >> price;

                std::cout << "Enter product type (Physical/Digital): ";
                std::cin >> type;

                if (type == "Physical") {
                    std::cout << "Quantity: ";
                    std::cin >> quantity;
                    PhysicalProduct* physicalProduct = new PhysicalProduct(id, name, price, quantity);
                    inventory.addProduct(physicalProduct);
                } else if (type == "Digital") {
                    std::cout << "Format: ";
                    std::cin >> format;
                    DigitalProduct* digitalProduct = new DigitalProduct(id, name, price, format);
                    inventory.addProduct(digitalProduct);
                } else {
                    std::cout << "Invalid product type!" << std::endl;
                }

                std::cout << "Product added successfully!" << std::endl;
                break;
            }
            case 2:
                inventory.displayInventory();
                break;
            case 3: {
                int productId, newQuantity;
                std::cout << "Enter product ID to update quantity: ";
                std::cin >> productId;

                std::cout << "Enter new quantity: ";
                std::cin >> newQuantity;

                inventory.updateProductQuantity(productId, newQuantity);
                break;
            }
            case 4: {
                std::string filename;
                std::cout << "Enter filename to save inventory: ";
                std::cin >> filename;
                inventory.saveToFile(filename);
                std::cout << "Inventory saved to file successfully!" << std::endl;
                break;
            }
            case 5: {
                std::string filename;
                std::cout << "Enter filename to load inventory: ";
                std::cin >> filename;
                inventory.loadFromFile(filename);
                std::cout << "Inventory loaded from file successfully!" << std::endl;
                break;
            }
            case 6: {
                std::string name;
                int customerId;

                std::cout << "Enter customer details:" << std::endl;
                std::cout << "Customer ID: ";
                std::cin >> customerId;

                std::cout << "Name: ";
                std::cin.ignore();  // clear the newline character from the buffer
                std::getline(std::cin, name);

                Customer customer(name, customerId);
                inventory.addCustomer(customer);

                std::cout << "Customer added successfully!" << std::endl;
                break;
            }
            case 7:
                inventory.displayCustomers();
                break;
            case 8:
                std::cout << "Exiting program..." << std::endl;
                return 0;
            default:
                std::cout << "Invalid choice. Please try again." << std::endl;
        }
    }
}
