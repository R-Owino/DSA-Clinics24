/* 
24. Swap Nodes in Pairs

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
given: 1 -> 2 -> 3 -> 4
swap: 2 -> 1 -> 4 -> 3

Input: head = [1,2,3]
Output: [2,1,3]
given: 1 -> 2 -> 3
swap: 2 -> 1 -> 3 
*/

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution;

impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		// create a dummy node
		let mut dummy = Some(Box::new(ListNode { val: 0, next: head}));
		let mut prev = dummy.as_mut();

		while let Some(node) = prev {
			// check there are 2 nodes to swap
			if node.next.is_some() && node.next.as_ref()?.next.is_some() {
				let mut first = node.next.take().unwrap();
				let mut second = first.next.take().unwrap();

				// perform the swap
				node.next = Some(second.clone());
				let first = Some(Box::new(ListNode {
					val: first.val,
					next: second.next.take(),
				}));
				node.next.as_mut()?.next = first;

				// next pair swap
				prev = node.next.as_mut()?.next.as_mut();
			} else {
				break;
			}
		}
		dummy.unwrap().next
	}
}

// convert Vec<i32> to Option<Box<ListNode>>
fn vec_to_linked_list(values: Vec<i32>) -> Option<Box<ListNode>> {
    let mut curr = None;
    for &val in values.iter().rev() {
        let mut new_node = Box::new(ListNode::new(val));
        new_node.next = curr;
        curr = Some(new_node);
    }
    curr
}

// convert Option<Box<ListNode>> to Vec<i32>
fn linked_list_to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut values = vec![];
    while let Some(node) = head {
        values.push(node.val);
        head = node.next;
    }
    values
}

fn main() {
	let head = vec_to_linked_list(vec![1,2,3,4,5]);
    let swaped_pairs = linked_list_to_vec(Solution::swap_pairs(head));
    println!("{:?}", swaped_pairs);
}
