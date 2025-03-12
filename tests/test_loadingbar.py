import time
from loadingbarcli import LoadingBar

def test_loading_bar():
    # Test basic functionality
    print("Testing basic loading bar...")
    bar = LoadingBar(total=100, length=50, fill='█', color="blue")
    for i in range(101):
        time.sleep(0.05)  # Simulate work being done
        bar.update(i)
    bar.finish()
    print("Basic loading bar test completed.\n")

def test_custom_colors():
    # Test loading bar with custom colors
    print("Testing loading bar with custom colors...")
    bar = LoadingBar(total=100, length=50, fill='█', color="green")
    for i in range(101):
        time.sleep(0.03)  # Simulate work being done
        bar.update(i)
    bar.finish()
    print("Custom colors test completed.\n")

def test_different_length():
    # Test loading bar with a different length
    print("Testing loading bar with a different length...")
    bar = LoadingBar(total=100, length=30, fill='#', color="red")
    for i in range(101):
        time.sleep(0.02)  # Simulate work being done
        bar.update(i)
    bar.finish()
    print("Different length test completed.\n")

def test_fast_progress():
    # Test loading bar with fast progress
    print("Testing loading bar with fast progress...")
    bar = LoadingBar(total=100, length=50, fill='*', color="yellow")
    for i in range(101):
        time.sleep(0.01)  # Simulate work being done
        bar.update(i)
    bar.finish()
    print("Fast progress test completed.\n")

if __name__ == "__main__":
    test_loading_bar()
    test_custom_colors()
    test_different_length()
    test_fast_progress()
    print("All tests completed successfully!")